# Copyright 2020, Trail of Bits. All rights reserved.

from .parser import BinaryParser, BinaryMetadataVisitor


class IDABinaryParser(BinaryParser):

    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        pass