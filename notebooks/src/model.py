from transformers import DistilBertModel
from torch import nn

class DistilBertForClassification(nn.Module):
    def __init__(self, num_classes=2):
        super(DistilBertForClassification, self).__init__()
        self.distilbert = DistilBertModel.from_pretrained('distilbert-base-uncased')

        for param in self.distilbert.parameters():
            param.requires_grad = False

        self.classifier = nn.Sequential(
            nn.Linear(self.distilbert.config.hidden_size, num_classes), 
            nn.Softmax(dim=-1)
        )

    def forward(self, input_ids, attention_mask=None):
        outputs = self.distilbert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]
        logits = self.classifier(cls_output)
        
        return logits