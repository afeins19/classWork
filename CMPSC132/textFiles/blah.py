def cc(s,k):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    cypher = alpha[k:len(alpha)]
    cypher+=alpha[0:k]
    print(cypher)
cc('test',0)