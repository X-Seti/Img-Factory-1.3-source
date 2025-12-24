#ifndef CFileParser_H
#define CFileParser_H

#include <string>
#include <fstream>

enum eEndian
{
	LITTLE_ENDIAN	=	0,
	BIG_ENDIAN		=	1
};

class CFileParser
{
public:
	CFileParser(void) :
		m_uiSeek(0),
		m_bReadAllAtOnce(true)
	{};

	static CFileParser*	getInstance(void);

	void				setEndian(eEndian eEndian) { m_eEndian = eEndian; }
	void				setReadAllAtOnce(bool bState) { m_bReadAllAtOnce = bState; }

	bool				open(std::string strPath, bool bBinaryMode);
	void				close(void);
	
	std::string			readString(unsigned long uiByteCount, bool bPeek = false);
	std::string			readStringUntilZero(bool bPeek = false);
	unsigned long		readULong(bool bPeek = false);
	unsigned short		readUShort(bool bPeek = false);
	unsigned char		readUChar(bool bPeek = false);
	
	std::string			readLine(void);

	void				seek(unsigned long uiSeek);
	bool				isEOF(void);

	//std::string			getFileContent(void) { return m_strFileContent; }
	std::string*		getFileContent(void) { return m_pFileContent; }
	void				setFileContent(std::string *pFileContent) { delete m_pFileContent; m_pFileContent = pFileContent; }
	
private:
	static CFileParser*	m_pInstance;
	eEndian				m_eEndian;

	bool				m_bReadAllAtOnce;

	//std::string			m_strFileContent;
	std::string*		m_pFileContent;
	unsigned long		m_uiSeek;

	std::ifstream		m_file;
	unsigned long		m_uiFileSize;
};

#endif