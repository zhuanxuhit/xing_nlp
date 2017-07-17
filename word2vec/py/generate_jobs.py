# 产生自动搜寻的脚本，寻找到最好的参数

head="""
#!/bin/bash
ROOT_DIR=/home/iknow/wc/jupyter/xing_nlp/word2vec
PY=$ROOT_DIR/word2vec.py
DATA_PATH=$ROOT_DIR/text8.small
EVAL_DATA=$ROOT_DIR/questions-words.txt
SAVE_PATH=$ROOT_DIR/temp

__cmd__
"""


train_cmd = "python $PY --train_data $DATA_PATH --eval_data $EVAL_DATA --save_path $SAVE_PATH"

def main():
    #--embedding_size 20 --learning_rate 1.0 --batch_size 48 --window_size 10
    def learning_rate(val):
        return "l{}".format(val), "--learning_rate {}".format(val)
    def embedding_size(val):
        return "e{}".format(val), "--embedding_size {}".format(val)
    def batch_size(val):
        return "b{}".format(val), "--batch_size {}".format(val)
    def window_size(val):
        return "b{}".format(val), "--window_size {}".format(val)

    funcs = [learning_rate, embedding_size, batch_size,  window_size]
    template = [1.0, 20, 48, 10]
    # embedding_size: 10 - 400
    # learning_rate: 0.0001 – 10
    # batch_size: 4– 512
    # window_size: 1 - 20
    params = []
    _embedding_size = range(10,410,10)
    _learning_rate = [0.0001,0.001,0.01,0.1,1,10]
    _batch_size = [4,8,16,32,64,128,256,512]
    _window_size = range(1,21,1)
    for e in _embedding_size:
        for l in _learning_rate:
            for b in _batch_size:
                for w in _window_size:
                    params.append([e,l,b,w])

    def get_name_cmd(paras):
        name = ""
        cmd = []
        for func, para in zip(funcs, paras):
            n, c = func(para)
            name += n
            cmd.append(c)

        name = name.replace(".", '')

        cmd = " ".join(cmd)
        return name, cmd
    # train
    for para in params:
        name, cmd = get_name_cmd(para)
        cmd = train_cmd + cmd
        # for train
        fn = "../jobs/{}.sh".format(name)
        f = open(fn, 'w')
        content = head.replace("__cmd__", cmd)
        # content = content.replace("__id__", name)
        # content = content.replace("__data_dir__", para[0])
        f.write(content)
        f.close()

if __name__ == "__main__":
    main()