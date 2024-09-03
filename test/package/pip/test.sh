#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# shellcheck disable=all
source /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartSetup
      rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
      rlRun "source \$TMT_PLAN_DATA/venv/bin/activate" 0 "Source the plan's virtual environment"
      # Secondary venv inheriting from the main virtual environment
      # keeps the plan's vnev clean
      rlRun "python3 -m venv --system-site-packages \$tmp/venv" 0 "Create the test's virtual environment"
      rlRun "deactivate && source \$tmp/venv/bin/activate" 0 "Source the test's virtual environment"
      rlRun "set -o pipefail"
    rlPhaseEnd

    rlPhaseStartTest
    	rlRun "pip install -v --no-build-isolation ." 0 "Install the test package"
    	rlRun -s "main" 0 "Run the test executable"
    	rlAssertGrep "Hello, World!" $rlRun_LOG
    rlPhaseEnd

    rlPhaseStartCleanup
      rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
