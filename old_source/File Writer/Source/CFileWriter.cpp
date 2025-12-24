#include "CFileWriter.h"
#include "CStringUtility.h"

using namespace std;

enum eEndian
{
	LITTLE_ENDIAN = 0,
	BIG_ENDIAN = 1
};

CFileWriter*	CFileWriter::m_pInstance = nullptr;

CFileWriter*	CFileWriter::getInstance(void)
{
	if (CFileWriter::m_pInstance == nullptr)
	{
		CFileWriter::m_pInstance = new CFileWriter;
	}
	return CFileWriter::m_pInstance;
}

void			CFileWriter::open(string strPath, bool bBinaryMode)
{
	m_file.open(strPath.c_str(), ofstream::in|ofstream::out|ofstream::trunc|(bBinaryMode ? ofstream::binary : 0));
}
void			CFileWriter::close(void)
{
	m_file.close();
}

void			CFileWriter::writeString(string strData, unsigned long uiByteCount)
{
	m_file.write(strData.c_str(), uiByteCount);
}
void			CFileWriter::writeULong(unsigned long uiData)
{
	m_file.write(CStringUtility::packULong(uiData, m_eEndian == BIG_ENDIAN).c_str(), 4);
}
void			CFileWriter::writeUShort(unsigned short usData)
{
	m_file.write(CStringUtility::packUShort(usData, m_eEndian == BIG_ENDIAN).c_str(), 2);
}
void			CFileWriter::writeUChar(unsigned char ucData)
{
	m_file.write(CStringUtility::packUChar(ucData).c_str(), 1);
}

string			CFileWriter::getFileContent(void)
{
	unsigned long uiLength = m_file.tellp();
	m_file.seekg(0, ios::beg);
	string strData;
	strData.resize(uiLength, '\0');
	m_file.read(&strData[0], uiLength);
	m_file.seekp(uiLength);
	return strData;
}
void			CFileWriter::seek(unsigned long uiPosition)
{
	m_file.seekp(uiPosition, ios::beg);
}