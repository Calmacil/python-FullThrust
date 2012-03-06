# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Lenoël Thomas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# * Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Ce fichier contient la classe Module, décrite ci-après. """


class Module(object):
    """Classe Module qui représente un set d'équipements regroupés
    ensembles.

    Un module est remplacé tout d'un bloc et comporte toujours les mêmes
    pièces d'équipemement, la plupart du temps des armes. Il est
    caractérisé par son nom et sa masse. Son coût est égal à celui des
    équipements qu'il comporte.
    """

    def __init__(self, nom="", nom_court="", masse="",
            forme={'lon': 0, 'lar': 0}):
        """Effectue des initialisations."""
        if not isinstance(forme, 'dict'):
            raise Exception('Mauvais argument: dictionnaire attendu.')
        self.nom = nom
        self.nom_court = nom_court
        self.masse = masse
        self.forme = forme
        self.composants = []

    def ajouter_equipement(self, equipement, pos={'x': 0, 'y': 0}):
        """Ajoute un équipement au module.

        **Arguments**
        equipement:     Equipement
        pos:            Dictonnaire contenant les coordonnées de l'équipement
            sur le module.
        """
        if not isinstance(equipement, 'Equipement'):
            raise Exception('Mauvais argument: dictionnaire attendu.')
        if (pos['x'] > self.composants['lon'] or
                pos['y'] > self.composants['lar']):
            raise Exception('Composant hors du module')
