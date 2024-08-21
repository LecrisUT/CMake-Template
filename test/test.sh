#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# shellcheck disable=all
source /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartSetup
      rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
      rlRun "set -o pipefail"
    rlPhaseEnd

    rlPhaseStartTest
    	rlRun "cmake -B $tmp/build --log-context -Wdev"
    	rlRun "cmake --build $tmp/build"
    	rlRun "ctest --test-dir $tmp/build --output-on-failure"
    rlPhaseEnd

    rlPhaseStartCleanup
      rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
