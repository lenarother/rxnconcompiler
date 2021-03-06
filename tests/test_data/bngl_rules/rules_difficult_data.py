#!/usr/bin/env python

# TODO: add ppi reactions

"""
rule_difficult_data.py contains dictionaries with examples of reactions
that produced eror in some point and are not included in other tests.
(e.g. <C1>; 1--2 Ste7--Ste11). 

One dict represents single system, that should run in BioNetGen.
{rxncon_quick_string: 'Rules': [rule1, rule2 ...], 'Tags': [rtype ...]}
"""


DEGRADATION = {
'Kin_P+_X': {
    'Rules': [
    'Kin + X(Kin~U) -> Kin + X(Kin~P)'],
    'Tags': [
    1, 'P+', 'no contingencies']},

'ins_ppi_IR': {
    'Rules':[
    'ins(IR) + IR(ins) <-> IR(ins!1).ins(IR!1)'],
    'Tags': [
    1, 'ppi', 'no contingencies']},

'a_ppi_IR': {
    'Rules':[
    'a(IR) + IR(a) <-> IR(a!1).a(IR!1)'],
    'Tags': [
    1, 'ppi', 'no contingencies']},

'X_DEG_ins; ! X_[Kin]-{P}; ! ins--IR': {
    'Rules':[
    'X(Kin~P) + IR(ins!1).ins(IR!1) -> X(Kin~P) + IR(ins)'],
    'Tags': [
    1, 'DEG', 'no contingencies']},
}

# This is not possible now
JANINA = {"""A_ppi_B
A_ppi_C
A_ppi_D
A_P+_E; ! <bool>
<bool>; OR <1+2>; OR <2+3>; OR <1+3>
<1+2>; ! A--B
<1+2>; ! A--C
<1+2>; x A--D
<2+3>; ! A--C
<2+3>; ! A--D
<2+3>; x A--B
<1+3>; ! A--B
<1+3>; ! A--D
<1+3>; x A--C""": { 
    'Rules': [
    'Kin + X(Kin~U) -> Kin + X(Kin~P)'],
    'Tags': [
    1, 'P+', 'no contingencies']}
}

JANINA2 = {
"""Fus3_ppi_Ste7; k- <C>
<C>; AND Ste5--Ste7; AND Ste5--Ste11""": { 
    'Rules': [
    'Kin + X(Kin~U) -> Kin + X(Kin~P)'],
    'Tags': [
    1, 'P+', 'no contingencies']}
}


BOOL_EXAMPLE = {
# required for <bool>
'''Cdc4_[WD40]_ppi_Tec1_[CPD]''': {
    'Rules': [
    'Cdc4(WD40) + Tec1(CPD) <-> Cdc4(WD40!1).Tec1(CPD!1)'],
    'Tags': [
    1, 'ppi', 'Cdc4', 'Tec1', 'no contingencies']},

# required for <bool>
'''Cdc4_[SCF]_ppi_SCF_[Cdc4]''': {
    'Rules': [
    'Cdc4(SCF) + SCF(Cdc4) <-> Cdc4(SCF!1).SCF(Cdc4!1)'],
    'Tags': [
    1, 'ppi', 'Cdc4', 'SCF', 'no contingencies']},

# required for <bool2>
'''Ste5_[MEK]_ppi_Ste7_[Ste5]''': {
    'Rules': [
    'Ste5(MEK) + Ste7(Ste5) <-> Ste5(MEK!1).Ste7(Ste5!1)'],
    'Tags': [
    1, 'ppi', 'Ste5', 'Ste7', 'no contingencies']},

# required for <bool2>
'''Fus3_[CD]_ppi_Ste7_[BDMAPK]''': {
    'Rules': [
    'Fus3(CD) + Ste7(BDMAPK) <-> Fus3(CD!1).Ste7(BDMAPK!1)'],
    'Tags': [
    1, 'ppi', 'Fus3', 'Ste7', 'no contingencies']},

'''SCF_Ub+_Tec1; ! <bool>
<bool>; AND Cdc4_[WD40]--Tec1_[CPD]; AND Cdc4_[SCF]--SCF_[Cdc4]''': {
    'Rules': [
    'Cdc4(SCF!2,WD40!1).SCF(Cdc4!2).Tec1(SCF~U,CPD!1) -> Cdc4(SCF!2,WD40!1).SCF(Cdc4!2).Tec1(SCF~Ub,CPD!1)'],
    'Tags': [
    1, 'Ub+', 'SCF', 'Tec1', 'contingencies', 'bool']},

'''Fus3_ppi_Ste5_[Unlock]; ! <bool2> 
<bool2>; AND Ste5_[MEK]--Ste7_[Ste5]; AND Fus3_[CD]--Ste7_[BDMAPK]''': {
    'Rules':[
    'Fus3(AssocSte5,CD!2).Ste5(MEK!1,Unlock).Ste7(BDMAPK!2,Ste5!1) <-> Fus3(AssocSte5!3,CD!2).Ste5(MEK!1,Unlock!3).Ste7(BDMAPK!2,Ste5!1)'],
    'Tags': [
    1, 'ppi', 'Fus3', 'Ptp3', 'contingencies', '!', 'difficault']},
}


DATA = [BOOL_EXAMPLE]