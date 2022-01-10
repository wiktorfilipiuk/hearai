import torch
import torch.nn as nn

class MultiFrameFeatureExtractor(nn.Module):
    """
    Class to extract features from every frame of the video.

    Input to the model should have shape NxCxHxW (frames x channels x height x width).

    Output from the model is a Tensor of shape NxM (count_of_frames x representation_size).

    Args:
        feature_extractor_name (str): the feature extractor.
    """

    def __init__(self,
                 feature_extractor):

        super().__init__()

        
        self.feature_extractor = feature_extractor


    def forward(self, x):
        frame_features = []

        for frame in x:
            frame = frame.unsqueeze(0)
            output = self.feature_extractor(frame).squeeze(0)
            frame_features.append(output)

        frame_features = torch.stack(frame_features, dim=0)
            
        return frame_features

