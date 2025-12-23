#ifndef CFileWriter_H
#define CFileWriter_H

#include <string>
#include <fstream>

enum eEndian;

class CFileWriter
{
public:
	static CFileWriter*		getInstance(void);
	
	void					setEndian(eEndian eEndian) { m_eEndian = eEndian; }
	
	void					open(std::string strPath, bool bBinaryMode);
	void					close(void);
	
	void					writeString(std::string strData, unsigned long uiByteCount);
	void					writeULong(unsigned long uiData);
	void					writeUShort(unsigned short usData);
	void					writeUChar(unsigned char ucData);

	std::string				getFileContent(void);
	void					seek(unsigned long uiPosition);
	
private:
	static CFileWriter*		m_pInstance;
	eEndian					m_eEndian;
	std::fstream			m_file;
};

#endif