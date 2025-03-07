from opensoundscape.torch.architectures import cnn_architectures
import pytest


def test_freeze_feature_extractor():
    """should disable grad on featur extractor but not classifier"""
    arch = cnn_architectures.resnet18(2, freeze_feature_extractor=True)
    assert not arch.parameters().__next__().requires_grad
    assert arch.fc.parameters().__next__().requires_grad


def test_modify_resnet():
    """test modifying number of output nodes"""
    arch = cnn_architectures.resnet18(10)
    assert arch.fc.out_features == 10


def test_freeze_params():
    """tests that model parameters are frozen"""
    arch = cnn_architectures.resnet18(100)
    cnn_architectures.freeze_params(arch)
    for param in arch.parameters():
        assert param.requires_grad == False


def test_resnet18():
    arch = cnn_architectures.resnet18(0, use_pretrained=False)


def test_resnet34():
    arch = cnn_architectures.resnet34(10, use_pretrained=False)


def test_resnet50():
    arch = cnn_architectures.resnet50(2000, use_pretrained=False)


def test_resnet101():
    arch = cnn_architectures.resnet101(4, use_pretrained=False)


def test_resnet152():
    arch = cnn_architectures.resnet152(3, use_pretrained=False)


def test_alexnet():
    arch = cnn_architectures.alexnet(2, use_pretrained=False)


def test_vgg11_bn():
    arch = cnn_architectures.vgg11_bn(2, use_pretrained=False)


def test_squeezenet1_0():
    arch = cnn_architectures.squeezenet1_0(10, use_pretrained=False)


def test_densenet121():
    arch = cnn_architectures.densenet121(111, use_pretrained=False)


def test_inception_v3():
    arch = cnn_architectures.inception_v3(1, use_pretrained=False)


def test_use_pretrained():
    arch = cnn_architectures.resnet101(4, use_pretrained=True)


def test_noninteger_output_nodes():
    with pytest.raises(TypeError):
        arch = cnn_architectures.resnet101(4.5)
