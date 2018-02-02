"""

        This is SlideRunner - An Open Source Annotation Tool 
        for Digital Histology Slides.

         Marc Aubreville, Pattern Recognition Lab, 
         Friedrich-Alexander University Erlangen-Nuremberg 
         marc.aubreville@fau.de

        If you use this software in research, please citer our paper:
        M. Aubreville, C. Bertram, R. Klopfleisch and A. Maier:
        SlideRunner - A Tool for Massive Cell Annotations in Whole Slide Images
        Bildverarbeitung fuer die Medizin 2018, Springer Verlag, Berlin-Heidelberg

"""

from enum import Enum

class UIMainMode (Enum):
    """
        GUI main modes
    """
    MODE_VIEW = 1
    MODE_ANNOTATE_SPOT = 2
    MODE_ANNOTATE_AREA = 3
    MODE_ANNOTATE_POLYGON = 4
    MODE_ANNOTATE_FLAG = 5
