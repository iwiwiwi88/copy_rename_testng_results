import file_service as fs
import result_gui_service as rgs
import config_service as cs
import config_gui_service as cgs

# ***************** SETUP DATA ***************************************************
props = cs.read_properties()
source_path=props["source_path"]+props["file_name"]
destination_path=props["destination_path"]
file_name=props["file_name"]

# ******************* METHODS ****************************************************


    
# ******************* MAIN ****************************************************
def run():
    if (cs.should_config_file_be_recreated()):
        cgs.present_user_config_form()
    else:
        formatted_file_name = fs.create_file_name(source_path)
        copy_rename_result = fs.copy_results_file_and_rename(source_path, destination_path, file_name, formatted_file_name)
        rgs.present_results(copy_rename_result, destination_path, formatted_file_name)
              
run()