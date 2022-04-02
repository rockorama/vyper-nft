import pytest
import brownie


def test_token_minted(mint, bob):
    mint(1, bob)


def test_token_uri(nft, mint):
    mint(123)
    assert nft.tokenURI(123) == "https://mynft.com/123.json"
