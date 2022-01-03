import pandas_read_xml as pdx
def main():
    df = pdx.read_xml("lab4_rasp.xml")
    df.to_csv('out.csv', index = None)
if __name__ == '__main__':
    main()