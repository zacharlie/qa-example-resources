# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingParameterExpression,
    QgsProcessingOutputString,
)
from qgis.PyQt.QtCore import QCoreApplication


class ReturnTrue(QgsProcessingAlgorithm):

    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ReturnTrue()

    def name(self):
        """
        Returns the unique algorithm name.
        """
        return 'returntrue'

    def displayName(self):
        """
        Returns the translated algorithm name.
        """
        return self.tr('Returns True')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to.
        """
        return self.tr('Example')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs
        to.
        """
        return 'example'

    def shortHelpString(self):
        """
        Returns a localised short help string for the algorithm.
        """
        return self.tr(
            'Algorithm that always returns true, '
        )

    def initAlgorithm(self, config=None):

        self.addOutput(
            QgsProcessingOutputString(
                self.OUTPUT,
                self.tr('True value')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        return {
            self.OUTPUT: True
        }
