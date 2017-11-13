""" config.py
"""

import argparse

parser = argparse.ArgumentParser('PGGAN')

## general settings.
parser.add_argument('--train_data_root', type=str, default='/home/nashory/data/CelebA/Img')
parser.add_argument('--random_seed', type=int, default=12345)
parser.add_argument('--use_cuda', type=bool, default=False)




## training parameters.
parser.add_argument('--lr', type=float, default=0.0002)
parser.add_argument('--nc', type=int, default=3)
parser.add_argument('--nz', type=int, default=512)
parser.add_argument('--ngf', type=int, default=512)
parser.add_argument('--ndf', type=int, default=512)
parser.add_argument('--TICK', type=int, default=1000)           # 1 tick = 1000 images = (1000/batch_size) iter.
parser.add_argument('--max_resl', type=int, default=10)          # 10 --> 1024
parser.add_argument('--trns_tick', type=int, default=40)        # transition tick
parser.add_argument('--stab_tick', type=int, default=40)        # stabilization tick


## network structure.
parser.add_argument('--flag_wn', type=bool, default=False)
parser.add_argument('--flag_bn', type=bool, default=False)
parser.add_argument('--flag_pixelwise', type=bool, default=False)
parser.add_argument('--flag_leaky', type=bool, default=True)
parser.add_argument('--flag_tanh', type=bool, default=True)
parser.add_argument('--flag_sigmoid', type=bool, default=True)



## optimizer setting.
parser.add_argument('--optimizer', type=str, default='adam')
parser.add_argument('--beta1', type=float, default=0.0)
parser.add_argument('--beta2', type=float, default=0.999)




## display and save setting.
parser.add_argument('--use_tensorboard', type=bool, default=True)


## parse and save config.
config, _ = parser.parse_known_args()
