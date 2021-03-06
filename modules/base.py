from ..byte_io_wmd import ByteIO


class PragmaBase:
    model = None

    @classmethod
    def set_model(cls, model):
        from ..pragma_model import PragmaModel
        cls.model: PragmaModel = model

    def to_file(self, writer: ByteIO):
        raise NotImplemented

    def from_file(self, reader: ByteIO):
        raise NotImplemented
