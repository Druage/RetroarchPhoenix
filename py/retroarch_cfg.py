import os
import sys

if sys.platform == "win32":
    RETRO_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'retroarch_v1.0'))
    PY_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'py'))
else:
    RETRO_PATH = ""
    
OUTPUT_CFG = RETRO_PATH + "\\retroarch.cfg"

def write_shader(data):
    file = RETRO_PATH + "\\shaders\\" + "retroarch.cgp"
    print("Wrote to: ", file)
    with open(file, "w") as retro_cgp:
        retro_cgp.seek(0)
        retro_cgp.write(data)

def read_shader(selected_shader):
    with open(selected_shader, "r") as shader_file:
        if ".cgp" in selected_shader:
            shader_data = shader_file.readlines()
            first_line = shader_data[0].split()
            num_of_shaders = int(first_line[2].split('"')[1])
            for i in range(0, num_of_shaders-1):
                for line in shader_data:
                    if "filter_linear{:}".format(str(i)) == line.split()[0]:
                        index_for_wrap = shader_data.index(line) + 1
                        shader_data[index_for_wrap] = 'wrap_mode{:} = "clamp_to_border"\n'.format(i)
                        break
            return write_shader("".join(shader_data))                
        else:
            cg_file = ['shaders = "1"\n', 'shader0 = ""', \
                       'wrap_mode0 = "clamp_to_border"\n', 'float_framebuffer0 = "false"\n']
            
            cg_file[1] = 'shader0 = "{:}"\n'.format(selected_shader)
            write_cg("".join(cg_file))
            
    config_data = get_config_data(PY_PATH + "\\retroarch.cfg")
    ammended_data = ammend_config(config_data)
    write_config(OUTPUT_CFG, ammended_data)

def write_cg(ammended_data):
    with open(RETRO_PATH + "\\shaders\\retroarch.cgp", "w") as ofile:
        ofile.seek(0)
        ofile.write(ammended_data)
        ofile.write('wrap_mode0 = "clamp_to_border"\n')
        ofile.write('float_framebuffer0 = "false"\n')

def get_config_data(cfg_file):
    with open(cfg_file, "r") as  infile:
        cfg_data = infile.readlines()
        return cfg_data
    
def ammend_config(data):
    with open(OUTPUT_CFG, "r") as infile:
        for line in infile:
            if "video_shader" == line.split()[0]:
                data[data.index(line)] = 'video_shader = ":\shaders/retroarch.cgp"\n'
                return data
        print("never found")

def write_config(file, new_data):
    with open(file, "w") as outfile:
        outfile.seek(0)
        outfile.write("".join(new_data))
    