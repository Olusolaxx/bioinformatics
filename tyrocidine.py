#    Copyright (C) 2019 Greenweaves Software Limited
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>
#
#    Utilities for mass spectroscopy

from spectrum import create_lookup,get_abbrev
from reference_tables import amino_acids

def cycloSpectrum(peptide):  # from helpers
    def get_pairs(index_range):
        n=len(index_range)
        return [(i,j) for i in index_range for j in range(i,i+n) if j!=i]
    augmented_peptide=peptide+peptide
    result=[sum(augmented_peptide[a:b]) for (a,b) in get_pairs(range(len(peptide)))]
    result.append(0)
    result.append(sum(peptide)) 
    result.sort()
    return result 

def linearSpectrum(peptide):
    def get_pairs():
        return [(i,j) for i in range(len(peptide)) for j in range(len(peptide)+1) if i<j]  
    result=[sum(peptide[i:j]) for (i,j) in get_pairs()] 
    #result.append(0)
    result.sort()
    return result 

def consistent(peptide,spectrum):
    def count(element,spect):
        return len ([s for s in spect if abs(s-element)<0.001])
    peptide_spectrum=linearSpectrum(peptide)
    for element in peptide_spectrum:
        if count(element,peptide_spectrum)>count(element,spectrum):
            return False
    return True

def sequence(spectrum,epsilon=0.0001):
    def isConsistent(peptide):
        print (peptide)
        for mass in linearSpectrum(peptide):
            if mass==0: continue
            abbrev = get_abbrev(mass,masses,pairs)
            if abs(mass-amino_acids[abbrev].mon_mass)>epsilon:
                return False
        return True
    
    def expand(List):
        return [peptide + [mass]  for peptide in List for mass in masses[:-1] if consistent(peptide + [mass],spectrum)]
    List = [[]]
    masses,pairs = create_lookup()
    print (masses)
    while len(List)>0:
        List = expand(List)
    return ''

if __name__=='__main__':

    print (
        sequence(
            [ 371.5,  375.4,  390.4,  392.2,  409.0,  420.2,  427.2,  443.3,  446.4,  461.3, 
              471.4,  477.4,  491.3,  505.3,  506.4,  519.2,  536.1,  546.5,  553.3,  562.3, 
              588.2,  600.3,  616.2,  617.4,  618.3,  633.4,  634.4,  636.2,  651.5,  652.4, 
              702.5,  703.4,  712.5,  718.3,  721.0,  730.3,  749.4,  762.6,  763.4,  764.4,
              779.6,  780.4,  781.4,  782.4,  797.3,  862.4,  876.4,  877.4,  878.6,  879.4,
              893.4,  894.4,  895.4,  896.5,  927.4,  944.4,  975.5,  976.5,  977.4,  979.4, 
             1005.5, 1007.5, 1022.5, 1023.7, 1024.5, 1039.5, 1040.3, 1042.5, 1043.4, 1057.5, 
             1119.6, 1120.6, 1137.6, 1138.6, 1139.5, 1156.5, 1157.6, 1168.6, 1171.6, 1185.4,
             1220.6, 1222.5, 1223.6, 1239.6, 1240.6, 1250.5, 1256.5, 1266.5, 1267.5, 1268.6]
        ))
    
