import os
import datetime
import time
from log_config import config_log

logger=config_log(str(__name__).split('\\')[-1])


def dir_state(path):
    try:
        files_list=os.listdir(path)
        current_state=dict.fromkeys(files_list)
        for file in files_list:
            modification_time=os.path.getmtime(file)
            m_time=datetime.datetime.fromtimestamp(modification_time)
            current_state[file]=m_time.strftime('%d:%m:%Y %H:%M:%S')
        return current_state
    except Exception as e:
        logger.error(e)

def monitoring(path):
    try:
        previous_state=dir_state(path)
        while True:
            time.sleep(10)
            current_state=dir_state(path)
            for file in previous_state.keys():
                if file in current_state.keys():
                    if current_state[file]>previous_state[file]:
                        logger.info('{} Modified'.format(file))
                elif file not in current_state.keys():
                    logger.info('{} Deleted'.format(file))
            for file in current_state.keys():
                if file not in previous_state.keys():
                    logger.info('{} Created'.format(file))
            previous_state=current_state
    except KeyboardInterrupt:
        logger.info('Monitoring Stopped by User')
    except Exception as e:
        logger.error(e)

def main():
    path = input("Enter directory path: ")
    os.chdir(path)
    logger.info('{} monitoring started'.format(path.split('\\')[-1]))
    monitoring(path)

if __name__=='__main__':

    main()
