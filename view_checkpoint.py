import tensorflow as tf

checkpoint_path = '/home/karenli/carla-experiments/agents/imitation/model/model.ckpt-450000'
output_file_path = '/home/karenli/carla-experiments/agents/imitation/checkpoint_variables.txt'  # Replace with your desired output file path

# Print all variables in the checkpoint
reader = tf.compat.v1.train.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()

with open(output_file_path, 'w') as f:
    for key in var_to_shape_map:
        f.write("Variable: {}, Shape: {}\n".format(key, var_to_shape_map[key]))
