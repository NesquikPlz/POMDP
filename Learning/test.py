import os
import pickle
import numpy as np
import torch as th
import matplotlib.pyplot as plt


path: str = 'Learning/dataset'
dataset_path = os.path.join(os.getcwd(), path)
dataset_filename = 'light_dark_long_mini.pickle'

# with open(os.path.join(dataset_path, dataset_filename), 'rb') as f:
#     dataset = pickle.load(f)

# print(len(dataset['observation']))

# observation, action, reward, next_state = [], [], [], []
# indices = np.random.choice(len(dataset['observation']), 4)
# for idx in indices:
#     observation.append(dataset['observation'][idx])
#     action.append(dataset['action'][idx])
#     reward.append(dataset['reward'][idx])
#     next_state.append(dataset['next_state'][idx])
# tiny_data = {
#     'observation': observation,
#     'action': action,
#     'reward': reward,
#     'next_state': next_state
# }
# with open(dataset_path + '/super_tiny_dataset.pickle', 'wb') as f:
#     pickle.dump(tiny_data, f)


# n=2
# data = []
# while n <= 32:
#     data.append(th.arange(1, n+1))
#     n += 1

# print(len(data))
# print(data)

# with open('data_test.pickle', 'wb') as f:
#     pickle.dump(data, f)


# with open(os.path.join(dataset_path, dataset_filename), 'rb') as f:
#     dataset = pickle.load(f)

# index = np.random.randint(len(dataset['observation']))
# print(len(dataset['observation']))
# print(index)

# observation = dataset['observation'][index]
# action = dataset['action'][index]
# reward = dataset['reward'][index]
# next_state = dataset['next_state'][index]
# traj_len = dataset['traj_len'][index]
# traj = {'observation': observation,
#             'action': action,
#             'reward': reward,
#             'next_state': next_state,
#             'traj_len': traj_len}

a = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 1], [2, 3, 4]])
print(a.shape)
print(np.unique(a, axis=0))
print(a)