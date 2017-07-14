import file_service as fs
import result_gui_service as rgs
import config_service as cs

# ***************** SETUP DATA ***************************************************
props = cs.read_properties()
in_path=props["in_path"]+props["file_name"]
out_path=props["out_path"]
file_name=props["file_name"]

# ******************* METHODS ****************************************************


    
# ******************* MAIN ****************************************************

formatted_file_name = fs.create_file_name(in_path)
copy_rename_result = fs.copy_results_file_and_rename(in_path, out_path, file_name, formatted_file_name)
cr_result = fs.results[copy_rename_result]

rgs.present_results(copy_rename_result, out_path, formatted_file_name)