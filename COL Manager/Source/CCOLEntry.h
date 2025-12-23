#ifndef CCOLEntry_H
#define CCOLEntry_H

#include <string>

struct CCOLEntry
{
	std::string			m_strVersion;
	unsigned long		m_uiFileSize;
	std::string			m_strModelName;
	unsigned short		m_usModelId;
	/*
	union {
		struct {
			float					m_fRadius;
			float					m_fCenter[3];
			float					m_fMin[3];
			float					m_fMax[3];
		}					version1;
		struct {
			float					m_fMin[3];
			float					m_fMax[3];
			float					m_fCenter[3];
			float					m_fRadius;
		}					version2_3;
	}					m_bounds;
	*/
	std::string			m_strTBounds;
	std::string			m_strHeaderVersion2;
	std::string			m_strHeaderVersion3;
	unsigned long		m_uiBodyStart;
	unsigned long		m_uiBodyLength;
};

#endif