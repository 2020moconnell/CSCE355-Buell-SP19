#!/usr/bin/perl -w

# Perl script for testing CSCE 355 a project submission on pluto

# Usage:
# $ project-test.pl <your-submission-directory-name>

# Appends to file "comments.txt" in your submission directory

# This script must be run under the bash shell!

# edit as needed:

# parent directory for your submission directory
$submissionRoot = "$ENV{HOME}/courses/csce355/fa10/project/submissions";
# directory holding the test files
$testSuiteDir = "$ENV{HOME}/courses/csce355/fa10/project/testFiles";
$simulateTestDir = "$testSuiteDir/simulator";
$minimizeTestDir = "$testSuiteDir/minimizer";
$searchTestDir = "$testSuiteDir/searcher";
$timeout = 11;			# seconds (I'm generous, aren't I?)

@simTestFiles = ("bigDFA", "biggerDFA", "handoutDFA", "randomDFA1",
		 "randomDFA2", "randomDFA3", "randomDFA4", "randomDFA5");

############ You should not have to edit below this line ##############

# Check existence of test suite directory
die "No test suite directory $testSuiteDir\n"
    unless -d $testSuiteDir;

#sub main
{
    if (@ARGV) {
	while (@ARGV) {
	    $uname = shift @ARGV;
	    process_user();
	}
    } else {
	opendir DIR, $submissionRoot
	    or die "Cannot open submission directory $submissionRoot ($!)\n";
	@usernames = readdir DIR;
	closedir DIR;

	while (@usernames) {
	    $uname = shift @usernames;
	    next if $uname =~ /^\./;
	    next unless -d "$submissionRoot/$uname";
	    process_user();
	}
    }
}


sub process_user {
    print(STDERR "Processing $uname\n\n");
    $udir = "$submissionRoot/$uname";
    die "No subdirectory corresponding to $uname ($!)\n"
	unless -d $udir;

    open(COMMENTS, ">> $udir/comments.txt");

    cmt("Comments for $uname -------- " . now() . "\n");

    chdir $udir;

    if (-e "compile") {
	cmt("  Compiling program ...");
	$command = `cat compile`;
	chomp $command;
	$rc = system($command);
	if ($rc >> 8) {
	    cmt(" failed\n");
	}
	else {
	    cmt(" succeeded\n");
	}
    }

    if (-e "simulate") {
	test_simulator();
    }
    elsif (-e "minimize") {
	# test_minimizer();
	print(STDERR "Skipping $uname (minimization); grade by hand\n");
    }
    elsif (-e "search") {
	# test_searcher();
	print(STDERR "Skipping $uname (search); grade by hand\n");
    }
    else {
	cmt("    No run command file for $uname\n");
    }

    report_summary();

    close COMMENTS;

    print(STDERR "\nDone.\nComments are in $uname/comments.txt\n");
}


sub test_simulator {

    print(STDERR "Errors msgs for $uname:\n");
    print(STDOUT "System msgs for $uname:\n");

    cmt("Testing DFA simulator:\n");

    $error_count = 0;

    $runCommand = `cat simulate`;
    chomp $runCommand;

    foreach $base (@simTestFiles) {
	$rc = system("cat $simulateTestDir/${base}.txt > DFA.txt");
	if ($rc >> 8) {
	    cmt("Copy of ${base}.txt to DFA.txt failed.\n");
	}

	cmt("  Running simulator on $base ...");

	cmt("\n   $runCommand < $simulateTestDir/${base}-strings.txt > ${base}-out.txt 2> ${base}-err.txt");
	eval {
	    local $SIG{ALRM} = sub { die "timed out\n" };
	    alarm $timeout;
	    $rc = system("$runCommand < $simulateTestDir/${base}-strings.txt > ${base}-out.txt 2> ${base}-err.txt");
	    alarm 0;
	};
	if ($@ && $@ eq "timed out\n") {
	    cmt("\n $@");		# program timed out before finishing
	    $error_count++;
	    unlink "${base}-out.txt"
		if -e "${base}-out.txt";
	    unlink "${base}-err.txt"
		if -e "${base}-err.txt";
	    next;
	}
	if ($rc >> 8) {
	    cmt("\n terminated abnormally\n");
	    # $error_count++;
	    if (-e "${base}-err.txt") {
		cmt("  Standard error output:\nvvvvv\n");
		$report = `cat ${base}-err.txt`;
		unlink "${base}-err.txt";
		chomp $report;
		cmt("$report\n^^^^^\n");
	    }
	}
	else {
	    cmt("\n terminated normally\n");
	    if (-e "${base}-err.txt") {
		cmt("  Standard error output:\nvvvvv\n");
		$report = `cat ${base}-err.txt`;
		unlink "${base}-err.txt";
		chomp $report;
		cmt("$report\n^^^^^\n");
	    }
	}

	if (!(-e "${base}-out.txt")) {
	    cmt("  output file ${base}-out.txt does not exist\n");
	    $error_count++;
	    next;
	}

	cmt("  ${base}-out.txt exists -- comparing acc/rej outcomes with solution file\n");

	$report = check_outcomes(${base});
	unlink "${base}-out.txt";
	chomp $report;
	if ($report eq '') {
	    cmt(" outcomes match\n");
	}
	else {
	    cmt(" outcomes differ:\nvvvvv\n$report\n^^^^^\n");
	    $error_count++;
	}
    }
}


sub check_outcomes {
    my ($base) = @_;
    my $report = '';

    my $solSeq = get_outcome_sequence("$simulateTestDir/${base}-out.txt");
    my $testSeq = get_outcome_sequence("${base}-out.txt");

    if ($solSeq ne $testSeq) {
	$report .= "    Outcomes differ:\n      $solSeq (solution)\n      $testSeq (yours)\n";
	$error_count++;
    }
    return $report;
}


sub get_outcome_sequence {
    my ($file) = @_;
    my $ret = '';
    my $src = `cat $file`;
    while ($src =~ /aCCept|rEJect/i) {
	$ret .= $& eq 'accept' ? 'A' : 'R';
	$src = $';
    }
    return $ret;
}


sub report_summary {
    cmt("######################################################\n");
    cmt("Summary for $uname:\n");

#     foreach $base (@simTestFiles) {
# 	cmt("  $base: ");
# 	$errors = '';
# 	if (-e "${base}-err.txt") {
# 	    $errors = `cat ${base}-err.txt`;
# 	    chomp $errors;
# 	}
# 	elsif ($errors eq '') {
# 	    cmt(" ok");
# 	}
# 	else {
# 	    cmt(" error message(s) (check appropriateness):\n");
# 	    cmt($errors);
# 	}
# 	cmt("\n");
#     }
    cmt("There were a total of $error_count errors found.\n");
    cmt("######################################################\n");
}


sub cmt {
    my ($str) = @_;
#  print $str;
    print(COMMENTS $str);
}


sub now {
    my $ret;

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
    $ret = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat')[$wday];
    $ret .= " ";
    $ret .= ('Jan','Feb','Mar','Apr','May','Jun','Jul',
	     'Aug','Sep','Oct','Nov','Dec')[$mon];
    $ret .= " $mday, ";
    $ret .= $year + 1900;
    $ret .= " at ${hour}:${min}:${sec} ";
    if ( $isdst ) {
	$ret .= "EDT";
    } else {
	$ret .= "EST";
    }
    return $ret;    
}
