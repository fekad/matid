"""
Defines a set of regressions tests that should be run succesfully before
anything is pushed to the central repository.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
import sys

import numpy as np
from ase import Atoms
from ase.visualize import view
import json

from systax import Classifier
from systax.classification import \
    Class0D, \
    Class1D, \
    Class2D, \
    Class3D, \
    Atom, \
    Molecule, \
    Crystal, \
    Material1D, \
    Material2D, \
    Unknown, \
    Surface


def get_atoms(filename):
    with open(filename, "r") as fin:
        data = json.load(fin)
    pos = data["positions"]
    cell = data["normalizedCell"]
    num = data["labels"]

    atoms = Atoms(
        scaled_positions=pos,
        cell=1e10*np.array(cell),
        symbols=num,
        pbc=True
    )

    return atoms


class Class2DTests(unittest.TestCase):
    """Tests for the Class2D systems found in the NOMAD Archve for Exciting and
    FHIAims.
    """
    # def test_1(self):
        # system = get_atoms("./exciting2/Class2D/C4B2F4N2.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_2(self):
        # system = get_atoms("./exciting2/Class2D/C12H10N2.json")
        # # view(system)

        # classifier = Classifier(max_cell_size=30)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_3(self):
        # """This is an amorphous surface.
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ba16Ge20O56.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_4(self):
        # """Looks like a complicated surface, but the cell cannot be found.
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ba16O40Si12.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

        # # view(classification.region.cell)
        # # print(classification)
        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_5(self):
        # """Too sparse for 2D-material.
        # """
        # system = get_atoms("./fhiaims5/Class2D/F2.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_6(self):
        # """Looks like a complicated surface, but the cell cannot be found.
        # Needs futher testing.
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ge12Mg12O36.json")
        # # view(system)

        # classifier = Classifier(pos_tol=0.35)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # # for vacancy in vacancies:
            # # print(vacancy.position)
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_7(self):
        # """Looks like a complicated surface, but the cell cannot be found.
        # Needs futher testing.
        # """
        # system = get_atoms("./fhiaims5/Class2D/Mg12O36Ti12.json")
        # # view(system)

        # classifier = Classifier(pos_tol=0.3, pos_tol_scaling=0.00)
        # # classifier = Classifier(pos_tol=0.35)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

        # print(adsorbates)

        # atoms = Atoms(cell=system.get_cell())
        # for vacancy in vacancies:
            # print(vacancy)
            # atoms += vacancy
        # view(atoms)

    # def test_8(self):
        # """Too sparse
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ne2.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_8(self):
        # """Too sparse
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ne2.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Class2D)

    # def test_9(self):
        # """Should be a pristine surface. Previously the max cell size was too
        # small.
        # """
        # system = get_atoms("./fhiaims5/Surface/Adsorbate/Ba16O48Si16.json")
        # # view(system)

        # classifier = Classifier(max_cell_size=12)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_9(self):
        # """All the adsorbates were not correctly identified. Increasing the
        # similarity threshold fixes the problem.
        # """
        # system = get_atoms("./fhiaims5/Surface/Adsorbate/C2Ba16O44Zr12.json")
        # # view(system)

        # classifier = Classifier(max_cell_size=12)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns

        # # Print adsorbates
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 6)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)
        # self.assertTrue(set(adsorbates) == set((68, 69, 70, 71, 72, 73)))

    # def test_10(self):
        # """This system is basically a very thick surface with one layer only.
        # Thus it is not classified as surface (only one layer) nor Material2D
        # (too thick).
        # """
        # system = get_atoms("./fhiaims5/Class2D/Ca32O80Zr24.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_11(self):
        # """The adsorbate in this system was not detected for an unknown reason.
        # The bug was caused by to multiple overlapping edges in the periodicity
        # graph.
        # """
        # system = get_atoms("./fhiaims5/Surface/Pristine/CCa16O16.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 1)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_12(self):
        # """Adsorbate was added to the cell for unknown reason. This bug was
        # caused by too low threshold for filtering graphs with size different
        # from the graphs where the seed atom is.
        # """
        # system = get_atoms("./fhiaims5/Surface/Vacancy+Adsorbate/H4Mg12O14.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 6)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_13(self):
        # """In this system the unit cell has duplicate entries for two atoms.
        # Reason is still unknown, but does not affect the search because they
        # are so close.
        # """
        # system = get_atoms("./fhiaims5/Surface/Pristine/Ca24O88Zr32.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_14(self):
        # """Wrong vacancy detected, wrong adsorbate, wrong interstitial. Cause
        # by a bug in wrapping coordinates during the region tracking.
        # """
        # system = get_atoms("./fhiaims5/Surface/Vacancy+Interstitial+Adsorbate/Mg12O36Si12.json")
        # # view(system)

        # classifier = Classifier()
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 0)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)

    # def test_15(self):
        # """Wrong vacancy detected, wrong adsorbate, wrong interstitial. The
        # position tolerance needs to be modified and the chemical environment
        # tolerance relaxed for correct classification.
        # """
        # system = get_atoms("./fhiaims5/Surface/Vacancy+Interstitial+Adsorbate/H2Mg61NiO62.json")
        # # view(system)

        # classifier = Classifier()
        # # classifier = Classifier(pos_tol=0.6, pos_tol_scaling=0.1)
        # classification = classifier.classify(system)
        # self.assertIsInstance(classification, Surface)

        # # Pristine
        # adsorbates = classification.adsorbates
        # interstitials = classification.interstitials
        # substitutions = classification.substitutions
        # vacancies = classification.vacancies
        # unknowns = classification.unknowns
        # self.assertEqual(len(vacancies), 0)
        # self.assertEqual(len(substitutions), 0)
        # self.assertEqual(len(adsorbates), 3)
        # self.assertEqual(len(unknowns), 0)
        # self.assertEqual(len(interstitials), 0)
        # self.assertTrue(set(adsorbates) == set((72, 124, 125)))

    def test_16(self):
        """Test the substitute detection on surfaces. All substitutes should be
        validated based on the chemical environment instead of the tesselation.
        """
        system = get_atoms("./fhiaims5/Surface//Adsorbate/CMg39NiO40.json")
        view(system)

        classifier = Classifier()
        classification = classifier.classify(system)
        self.assertIsInstance(classification, Surface)

        # Adsorbate + Substitution
        adsorbates = classification.adsorbates
        interstitials = classification.interstitials
        substitutions = classification.substitutions
        vacancies = classification.vacancies
        unknowns = classification.unknowns
        self.assertEqual(len(vacancies), 0)
        self.assertEqual(len(substitutions), 1)
        self.assertEqual(len(adsorbates), 1)
        self.assertEqual(len(unknowns), 0)
        self.assertEqual(len(interstitials), 0)
        self.assertTrue(set(adsorbates) == set([80]))
        self.assertTrue(substitutions[0].index == 65)

if __name__ == '__main__':
    suites = []
    suites.append(unittest.TestLoader().loadTestsFromTestCase(Class2DTests))

    alltests = unittest.TestSuite(suites)
    result = unittest.TextTestRunner(verbosity=0).run(alltests)

    # We need to return a non-zero exit code for the gitlab CI to detect errors
    sys.exit(not result.wasSuccessful())
