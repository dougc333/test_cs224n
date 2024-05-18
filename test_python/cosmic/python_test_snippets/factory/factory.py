import pathlib
from abc import ABC, abstractmethod


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self)-> VideoExporter:
        pass
    @abstractmethod
    def get_audio_exporter(self)-> AudioExporter:
        pass

class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self,video_data):
        pass
    @abstractmethod
    def do_export(self,folder:pathlib.Path):
        pass

class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self,audio_data):
        pass
    @abstractmethod
    def do_export(self,folder:pathlib.Path):
        pass 

class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()



class LosslessVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        return super().prepare_export(video_data)

    def do_export(self, folder: pathlib.Path):
        return super().do_export(folder)


class H264BPVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        return super().prepare_export(video_data)
    def do_export(self, folder: pathlib.Path):
        return super().do_export(folder)
class H264Hi422PVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        return super().prepare_export(video_data)
    def do_export(self, folder: pathlib.Path):
        return super().do_export(folder)
        

class AACAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        return super().prepare_export(audio_data)

    def do_export(self, folder: pathlib.Path):
        return super().do_export(folder)
    
class WAVAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        return super().prepare_export(audio_data)
    
    def do_export(self, folder: pathlib.Path):
        return super().do_export(folder)

def read_exporter()->ExporterFactory:
    factories = {
        "low":FastExporter(),
        "high":HighQualityExporter(),
        "master":MasterQualityExporter()
    }
    while 1:
        export_quality = input("Enter low,high,master:")
        if export_quality in factories:
            return factories[export_quality]
        print("unknown input")

#main has low cohesion
#not extensible easily...have rto modify if else statements
def main():
    fac = read_exporter()

    video_exporter:fac.get_video_exporter()
    audio_exporter:fac.get_audio_exporter()

    
    
    video_exporter.prepare_export("placeholder")
    audio_exporter.prepare_export("placeholder")
    folder=pathlib.Path("temp")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

    

if __name__=="__main__":
    main()

