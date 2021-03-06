#!/usr/bin/env python

"""
Unit tests fror complex_builder module.
"""

from unittest import main, TestCase

from rxnconcompiler.biological_complex.biological_complex import BiologicalComplex
from rxnconcompiler.biological_complex.complex_builder import ComplexBuilder
from rxnconcompiler.molecule.state import get_state
from rxnconcompiler.molecule.molecule import Molecule


class BiologicalComplexBuilderTests(TestCase):
    """
    Unit Tests for ComplexBuilder class.
    """
    def setUp(self):
        """Builds a large 9 moleculs complex."""
        self.comp = BiologicalComplex()
        state_strings = ['A--B', 'A--C', 'A--D', 'B--E', 'B--F', \
                         'E--K', 'E--J', 'D--G', 'D--H']
        state_objects = [get_state(state) for state in state_strings]
        for state in state_objects:
            self.comp.add_state(state)
        self.comp.cid = '1' 

    def test_complex(self):
        """Tests whether complex in the setup is correctly built."""
        self.assertEqual(len(self.comp.molecules), 10)
        mol = self.comp.get_molecules('A')[0]
        self.assertEqual(len(mol.binding_partners), 3)
        mol = self.comp.get_molecules('C')[0]
        self.assertEqual(len(mol.binding_partners), 1)
        
    def test_get_states_from_complex(self):
        """"""
        mol = self.comp.get_molecules('A')[0]
        builder = ComplexBuilder()
        states = builder.get_states_from_complex(self.comp, mol)
        level1 = ['A_[AssocB]--B_[AssocA]', 'A_[AssocC]--C_[AssocA]', 'A_[AssocD]--D_[AssocA]']
        level2 = ['B_[AssocE]--E_[AssocB]', 'B_[AssocF]--F_[AssocB]', 'D_[AssocG]--G_[AssocD]', 'D_[AssocH]--H_[AssocD]']
        level3 = ['E_[AssocK]--K_[AssocE]', 'E_[AssocJ]--J_[AssocE]']
        for state in states[:3]:
            self.assertTrue(str(state) in level1)
        for state in states[3:7]:
            self.assertTrue(str(state) in level2)
        for state in states[7:]:
            self.assertTrue(str(state) in level3)

    def test_built_negative_complexes(self):
        """"""
        mol = self.comp.get_molecules('A')[0]
        builder = ComplexBuilder()
        negative = builder.build_negative_complexes(self.comp, mol)
        self.assertTrue(negative[-2].get_molecules('A')[0].binding_sites)
        self.assertTrue(len(negative), 9)

    def test_get_branches(self):
        """"""
        self.assertEqual(len(self.comp.get_branches('A')), 6)
        self.assertEqual(len(self.comp.get_top_branches('A')), 3)

    def test_paths(self):
        """"""
        result = '[[K, E, B, A, D, H]]'
        self.assertEqual(str(self.comp.get_paths(Molecule('K'), Molecule('H'))), result)
        result = '[K, E, B, A, D, H]'
        self.assertEqual(str(self.comp.get_shortest_path(Molecule('K'), Molecule('H'))), result)

    def test_add(self):
        comp_sec = BiologicalComplex()
        state_strings = ['A--B', 'A--C', 'A--K', 'K--Z']
        state_objects = [get_state(state) for state in state_strings]
        for state in state_objects:
            comp_sec.add_state(state)
        comp_sec.cid = '2'
        result = 'Complex: A, B, C, D, E, F, G, H, J, K, K, Z'
        self.assertEqual(str(self.comp.complex_addition(comp_sec, Molecule('A'))), result)


if __name__ == '__main__':
    main()
