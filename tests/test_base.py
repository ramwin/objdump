import unittest

from objdump.base import get_function_assemble


MAIN_CONTENT = """000000000000114f <main>:
    114f:	55                   	push   %rbp
    1150:	48 89 e5             	mov    %rsp,%rbp
    1153:	48 83 ec 10          	sub    $0x10,%rsp
    1157:	b8 00 00 00 00       	mov    $0x0,%eax
    115c:	e8 d7 2e 00 00       	call   4038 <_end>
    1161:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1164:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1167:	89 c6                	mov    %eax,%esi
    1169:	48 8d 05 94 0e 00 00 	lea    0xe94(%rip),%rax        # 2004 <_IO_stdin_used+0x4>
    1170:	48 89 c7             	mov    %rax,%rdi
    1173:	b8 00 00 00 00       	mov    $0x0,%eax
    1178:	e8 b3 fe ff ff       	call   1030 <printf@plt>
    117d:	b8 00 00 00 00       	mov    $0x0,%eax
    1182:	c9                   	leave  
    1183:	c3                   	ret    """


class Test(unittest.TestCase):

    def test(self):
        res = get_function_assemble("tests/example/a.out", "main")
        self.assertEqual(
            MAIN_CONTENT,
            res
        )
