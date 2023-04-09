import soundfile as sf
import librosa


temp = ''

def replace():
    global temp
    with open('transcript.v.1.4.txt', encoding='UTF8') as f:
        for line in f:
            line = line.split('|')
            line0, line2 = line[0], line[2]
            y, _ = librosa.load('kss/'+line0, sr=44100)
            data = librosa.resample(y, orig_sr=44100, target_sr=22050)
            sf.write('kss_resample/'+line0, data, samplerate=22050, subtype='PCM_16')
            temp += str('dataset/kss_resample/'+line0 + '|0|' + line2+'\n')

    with open('transcript.replace.txt', 'w', encoding='UTF8') as f:
        f.write(temp)




if __name__ == "__main__":
    replace()