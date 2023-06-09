
import sys
import os
import comtypes.client

input_folder_path = "C:\\Users\\sure\\Desktop\\Company\\동욱전임전달용\\변환폴더"
output_folder_path = "C:\\Users\\sure\\Desktop\\Company\\동욱전임전달용\\출력폴더"
input_file_paths = os.listdir(input_folder_path)

for input_file_name in input_file_paths:

    if not input_file_name.lower().endswith((".ppt", ".pptx")):
        continue

    input_file_path = os.path.join(input_folder_path, input_file_name)

    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    slides = powerpoint.Presentations.Open(input_file_path)

    file_name = os.path.splitext(input_file_name)[0]
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")

    slides.SaveAs(output_file_path, FileFormat=32)
    slides.Close()