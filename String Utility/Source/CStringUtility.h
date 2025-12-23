#ifndef CStringUtility_H
#define CStringUtility_H

#include <atlstr.h>
#include <string>
#include <vector>
#include <deque>

class CStringUtility
{
public:
	static std::vector<std::string>			split(std::string strString, std::string strToken);
	static std::string						join(std::vector<std::string>& vecTokens, std::string strDelimiter);
	static std::vector<std::string>			combineVectors(std::vector<std::string>& vecVector1, std::vector<std::string>& vecVector2);
	static std::deque<std::string>			convertVectorToDeque(std::vector<std::string>& vecVector);
	static std::vector<std::string>			toUpperCaseVector(std::vector<std::string>& vecVector);
	static unsigned long					findVectorKey(std::vector<std::string>& vecVector, std::string strValue);
	static std::string						replace(std::string strString, std::string strFind, std::string strReplace);
	static std::string						packULong(unsigned long uiULong, bool bBigEndian = true);
	static std::string						packUShort(unsigned short usUShort, bool bBigEndian = true);
	static std::string						packUChar(unsigned char ucUChar);
	static unsigned long					unpackULong(std::string strData, bool bBigEndian = true);
	static unsigned short					unpackUShort(std::string strData, bool bBigEndian = true);
	static unsigned char					unpackUChar(std::string strData);
	static std::string						toString(int iNumber);
	static int								toNumber(std::string strText);
	static unsigned long					toULong(std::string strString);
	static signed long						toLong(std::string strString);
	static float							toFloat(std::string strString);
	static std::string						trim(std::string strString);
	static std::string						ltrim(std::string strString);
	static std::string						rtrim(std::string strString);
	static std::string						rtrimFromLeft(std::string strString);
	static std::string						zeroPad(std::string strData, unsigned long uiPadLength);
	static std::string						toUpperCase(std::string strString);
	static std::string						convertCStringToStdString(CString str)
	{
		CT2CA pszConvertedAnsiString(str);
		return std::string(pszConvertedAnsiString);
	}
	static std::wstring						convertStdStringToStdWString(std::string str)
	{
		int iLength = MultiByteToWideChar(0, 0, str.c_str(), str.length() + 1, 0, 0);
		WCHAR *wstr = new WCHAR[iLength + 1];
		MultiByteToWideChar(0, 0, str.c_str(), str.length() + 1, wstr, iLength + 1);
		wstr[iLength] = 0;
		std::wstring wstr2(wstr);
		delete wstr;
		return wstr2;
	}
	static std::string						convertStdWStringToStdString(std::wstring str)
	{
		int len;
		int slength = (int)str.length() + 1;
		len = WideCharToMultiByte(CP_ACP, 0, str.c_str(), slength, 0, 0, 0, 0);
		char* buf = new char[len];
		WideCharToMultiByte(CP_ACP, 0, str.c_str(), slength, buf, len, 0, 0);
		std::string r(buf);
		delete[] buf;
		return r;
	}
};

#endif