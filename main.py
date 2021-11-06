import torch

print(f'''
	cuda enable: {torch.cuda.is_available()}
	current_device: {torch.cuda.current_device()}
	device: {torch.cuda.device(0)}
	device_count: {torch.cuda.device_count()}
	get_device_name: {torch.cuda.get_device_name(0)}
''')
