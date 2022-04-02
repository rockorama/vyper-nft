import pytest
from brownie import accounts


@pytest.fixture(scope="function", autouse=True)
def shared_setup(fn_isolation):
    pass


############
# Accounts #
############


@pytest.fixture
def owner(accounts):
    yield accounts[0]


@pytest.fixture
def bob(accounts):
    yield accounts[1]


@pytest.fixture
def alice(accounts):
    yield accounts[2]


##################
# NFT Contract #
##################


@pytest.fixture
def nft(NFT, owner):
    nft_contract = owner.deploy(NFT, "My First NFT", "NFT", "https://mynft.com/")
    assert nft_contract.name() == "My First NFT"
    assert nft_contract.symbol() == "NFT"
    yield nft_contract


@pytest.fixture
def mint(nft, owner, bob):
    def mint(id, receiver=bob):
        nft.mint(receiver, id, {"from": owner})
        assert nft.balanceOf(receiver) == 1
        assert nft.ownerOf(id) == receiver

    yield mint
