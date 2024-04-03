# 将CMLRdataset的视频和音频进行合并
for video_dir in CMLRdataset/video/s*; do
    if [ -d "$video_dir" ]; then
        s_dir="${video_dir##*/}"
        audio_dir="CMLRdataset/audio/${s_dir}"
        for date_dir in "$video_dir"/*; do
            if [ -d "$date_dir" ]; then
                date="${date_dir##*/}"
                for video_file in "$date_dir"/*.mp4; do
                    audio_file="${audio_dir}/${date}/${video_file##*/}"
                    audio_file="${audio_file%.*}.wav"
                    output_dir="cmlr_preprocessed/${s_dir}/${date}"
                    mkdir -p "$output_dir"
                    output_file="${output_dir}/${video_file##*/}"
                    ffmpeg -i "$video_file" -i "$audio_file" -ar 16000 -acodec aac -c:v copy -strict experimental "$output_file"
                done
            fi
        done
    fi
done