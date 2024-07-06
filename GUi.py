import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

label1 = sg.Text("Select archive:")
input1 = sg.InputText(tooltip='select files')
choose_button_files = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text("select directory:")
input2 = sg.InputText(tooltip='select destination directory')
choose_button_directory = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", font=('Helvetica', 10),
                   layout=[[label1, input1, choose_button_files],
                           [label2 ,input2, choose_button_directory],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    archive_path= values['archive']
    dest_dir = values['folder']
    extract_archive(archive_path, dest_dir)
    window['output'].update(value="Extraction Completed")

    if event == sg.WINDOW_CLOSED:
        break
window.close()

