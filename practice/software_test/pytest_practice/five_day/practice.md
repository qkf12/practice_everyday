#### pytest
1. **参数化**
   ```python
    def 函数名(形参):
        等等。。。



    @pytest.mark.parametrize("形参,expected",[
        (测试参数,expected),
        ....

    ])

    def test_测试函数(形参,expected):
        assert 函数(形参)  == expected
   ```


2. 四种覆盖方法
   - 语法覆盖
        - 跑通一遍<真值>
        - 后再跑一边else(前提是有else 如果没有就不用写)
   - 判断覆盖
        - 无论有没有else 
        - 都要测一遍<真值>和<假值>  
   - 条件覆盖
        - 专门测试大方向下的小条件
        - 缺点是可能进不去true的条件 
   - 条件判断覆盖
        - 全方位判断


   