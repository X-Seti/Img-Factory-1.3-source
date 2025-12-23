#include "CFileParser.h"
#include "CFileUtility.h"
#include "CStringUtility.h"
#include "CDebugger.h"

using namespace std;

CFileParser*	CFileParser::m_pInstance = nullptr;

CFileParser*	CFileParser::getInstance(void)
{
	if (CFileParser::m_pInstance == nullptr)
	{
		CFileParser::m_pInstance = new CFileParser;
	}
	return CFileParser::m_pInstance;
}

bool			CFileParser::open(string strPath, bool bBinaryMode)
{
	m_uiSeek = 0;
	if (m_bReadAllAtOnce)
	{
		//m_strFileContent = CFileUtility::getFileContent(strPath, bBinaryMode);
		m_pFileContent = CFileUtility::getFileContentPointer(strPath, bBinaryMode);
		//return m_strFileContent != "";
		//return (*m_pFileContent) != "";

		return m_pFileContent->length() != 0;
	}
	else
	{
		m_file.open(strPath, ios::in | (bBinaryMode ? ios::binary : 0));
		
		if (m_file.is_open())
		{
			m_file.seekg(0, SEEK_END);
			m_uiFileSize = m_file.tellg();
			m_file.seekg(0, SEEK_SET);
		}

		return m_file.is_open();
	}
}
void			CFileParser::close(void)
{
	m_uiSeek = 0;
	if (m_bReadAllAtOnce)
	{
		//m_strFileContent = "";
		*m_pFileContent = "";
		delete m_pFileContent;
	}
	else
	{
		m_file.close();
	}
}

string		CFileParser::readString(unsigned long uiByteCount, bool bPeek)
{
	string strData;
	if (m_bReadAllAtOnce)
	{
		//string strData = m_strFileContent.substr(m_uiSeek, uiByteCount);
		strData = m_pFileContent->substr(m_uiSeek, uiByteCount);
	}
	else
	{
		char *pData = new char[uiByteCount];
		m_file.read(pData, uiByteCount);
		strData.append(pData, uiByteCount);
		delete pData;
	}
	if (!bPeek)
	{
		m_uiSeek += uiByteCount;
	}
	return strData;
}
string			CFileParser::readStringUntilZero(bool bPeek)
{
	string strData;
	unsigned long uiLength;
	if (m_bReadAllAtOnce)
	{
		unsigned long uiPosition = m_pFileContent->find('\0', m_uiSeek);
		uiLength = uiPosition - m_uiSeek;
		strData = m_pFileContent->substr(m_uiSeek, uiLength);
	}
	else
	{
	}
	if (!bPeek)
	{
		m_uiSeek += uiLength + 1;
	}
	return strData;
}
unsigned long	CFileParser::readULong(bool bPeek)
{
	unsigned long uiData;
	if (m_bReadAllAtOnce)
	{
		//unsigned long uiData = CStringUtility::unpackULong(m_strFileContent.substr(m_uiSeek, 4), m_eEndian == BIG_ENDIAN);
		uiData = CStringUtility::unpackULong(m_pFileContent->substr(m_uiSeek, 4), m_eEndian == BIG_ENDIAN);
	}
	else
	{
		char cData[4];
		m_file.read(cData, 4);
		uiData = CStringUtility::unpackULong(cData, m_eEndian == BIG_ENDIAN);
	}
	if (!bPeek)
	{
		m_uiSeek += 4;
	}
	return uiData;
}
unsigned short	CFileParser::readUShort(bool bPeek)
{
	unsigned short usData;
	if (m_bReadAllAtOnce)
	{
		//unsigned short usData = CStringUtility::unpackUShort(m_strFileContent.substr(m_uiSeek, 2), m_eEndian == BIG_ENDIAN);
		usData = CStringUtility::unpackUShort(m_pFileContent->substr(m_uiSeek, 2), m_eEndian == BIG_ENDIAN);
	}
	else
	{
		char cData[2];
		m_file.read(cData, 2);
		usData = CStringUtility::unpackULong(cData, m_eEndian == BIG_ENDIAN);
	}
	if (!bPeek)
	{
		m_uiSeek += 2;
	}
	return usData;
}
unsigned char	CFileParser::readUChar(bool bPeek)
{
	unsigned char ucData;
	if (m_bReadAllAtOnce)
	{
		//unsigned char ucData = CStringUtility::unpackUChar(m_strFileContent.substr(m_uiSeek, 1));
		ucData = CStringUtility::unpackUChar(m_pFileContent->substr(m_uiSeek, 1));
	}
	else
	{
		char cData[1];
		m_file.read(cData, 1);
		ucData = CStringUtility::unpackULong(cData, m_eEndian == BIG_ENDIAN);
	}
	if (!bPeek)
	{
		m_uiSeek++;
	}
	return ucData;
}

string			CFileParser::readLine(void)
{
	if (m_bReadAllAtOnce)
	{
	}
	else
	{
		string strLine = "";
		getline(m_file, strLine);
		return strLine;
	}
}

void			CFileParser::seek(unsigned long uiSeek)
{
	if (m_bReadAllAtOnce)
	{
		m_uiSeek = uiSeek;
	}
	else
	{
		m_file.seekg(uiSeek);
	}
}
bool			CFileParser::isEOF(void)
{
	if (m_bReadAllAtOnce)
	{
		//return m_uiSeek >= m_strFileContent.length();
		return m_uiSeek >= m_pFileContent->length();
	}
	else
	{
		unsigned long uiSeek = m_file.tellg();
		return uiSeek >= m_uiFileSize;
	}
}