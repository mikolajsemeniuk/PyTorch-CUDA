import torch

print(f'''
	cuda enable: {torch.cuda.is_available()}
	current_device: {torch.cuda.current_device()}
	device: {torch.cuda.device(0)}
	device_count: {torch.cuda.device_count()}
	get_device_name: {torch.cuda.get_device_name(0)}
''')
'''
	cuda enable: True
        current_device: 0
        device: <torch.cuda.device object at 0x000001FC1984DCD0>
        device_count: 1
        get_device_name: NVIDIA GeForce GTX 1650 Ti
'''
