#!/usr/bin/env python

import storm_analysis


def test_rcc():

    mlist_name = storm_analysis.get_data("test/data/test_drift_mlist.bin")
    drift_name = storm_analysis.get_path_output_test("test_drift.txt")

    from storm_analysis.rcc.rcc_drift_correction import rccDriftCorrection
    rccDriftCorrection(mlist_name, drift_name, 2000, 1, True, False)


if (__name__ == "__main__"):
    test_rcc()
