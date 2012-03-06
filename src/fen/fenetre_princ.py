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

""" Ce fichier contient la classe FenetrePrinc décrite ci-dessous. """

from fen.base.base_fenetre_princ import BaseFenetrePrinc
from PyQt4.QtCore import pyqtSlot as Slot


class FenetrePrinc(BaseFenetrePrinc):
    """ classe FenetrePrinc

    Cette classe définit les évènements et les actions pour la fenetre
    principale de PyFt. Elle étend fen.base.BaseFenetrePrinc.
    """

    def __init__(self, parent=None):
        """ Fait des initialisations. """
        super(FenetrePrinc, self).__init__(parent)

        self.a_quit.triggered.connect(self.onQuitter)
        self.mFic.addAction(self.a_quit)

    @Slot()
    def onQuitter(self):
        """ Provoque la fermeture du programme. """
        self.close()
