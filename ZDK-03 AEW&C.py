Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import multiprocessing, logging
logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)
logger.warning('doomed')
[WARNING/MainProcess] doomed
m = multiprocessing.Manager()
del m
[INFO/MainProcess] sending shutdown message to manager
