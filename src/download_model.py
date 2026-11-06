import torch
from facenet_pytorch import InceptionResnetV1
model = InceptionResnetV1(pretrained="vggface2")
torch.save(model.state_dict(), "models/inception_vggface2.pth")
print("model saved")
