import textwrap

from pipenv.cmdparse import Script
import pytest


@pytest.mark.run
@pytest.mark.script
def test_parse():
    script = Script.parse(['python', '-c', "print('hello')"])
    assert script.command == 'python'
    assert script.args == ['-c', "print('hello')"], script


@pytest.mark.run
@pytest.mark.script
def test_cmdify():
    script = Script.parse(['python', '-c', "print('hello')"])
    cmd = script.cmdify(['--verbose'])
    assert cmd == '"python" "-c" "print(\'hello\')" "--verbose"', script


@pytest.mark.run
@pytest.mark.script
def test_cmdify_complex():
    script = Script.parse(' '.join([
        '"C:\\Program Files\\Python36\\python.exe" -c',
        """ "print(\'Double quote: \\\"\')" """.strip(),
    ]))
    assert script.cmdify([]) == ' '.join([
        '"C:\\Program Files\\Python36\\python.exe"',
        '"-c"',
        """ "print(\'Double quote: \\\"\')" """.strip(),
    ]), script
