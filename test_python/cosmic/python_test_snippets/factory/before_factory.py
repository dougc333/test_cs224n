import pathlib


import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self,video_data):
        pass
    @abstractmethod
    def do_export(self,folder:pathlib.Path):
        pass

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
        
class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self,audio_data):
        pass
    @abstractmethod
    def do_export(self,folder:pathlib.Path):
        pass 

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
#main has low cohesion
#not extensible easily...have rto modify if else statements
def main():
    export_quality:str
    while 1:
        export_quality = input("Enter low,high,master:")
        if export_quality in {'low','high','master'}:
            break
        print("unknown input")
    video_exporter:VideoExporter
    audio_exporter:AudioExporter
    if export_quality=='low':
        video_exporter = H264BPVideoExporter()
        audio_exporter = WAVAudioExporter()
    elif export_quality == 'high':
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()
    video_exporter.prepare_export("placeholder")
    audio_exporter.prepare_export("placeholder")
    folder=pathlib.Path("temp")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

    

if __name__=="__main__":
    main()

