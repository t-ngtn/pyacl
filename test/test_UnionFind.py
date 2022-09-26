from atcoder.UnionFind import UnionFind


def test_UnionFind():
    uf = UnionFind(3)
    uf.unite(1, 2)
    assert uf.is_same_group(1, 2)
    assert not (uf.is_same_group(1, 3))
    assert uf.count(1) == 2
    assert uf.find_root(1) == uf.find_root(2)
