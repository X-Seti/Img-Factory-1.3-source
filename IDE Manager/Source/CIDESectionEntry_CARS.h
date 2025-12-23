#ifndef CIDESectionEntry_CARS_H
#define CIDESectionEntry_CARS_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_CARS : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	std::string					m_strVehicleType;
	std::string					m_strHandlingId;
	std::string					m_strGameName;
	std::string					m_strAnimationFile;
	std::string					m_strVehicleClass;
	unsigned long				m_uiSpawnFrequency;
	unsigned long				m_uiUnknown1;
	unsigned long				m_uiUnknown2;
	unsigned long				m_uiWheelModelId;
	float						m_fWheelScaleFront;
	float						m_fWheelScaleRear;
	float						m_fWheelScale;
	unsigned long				m_uiUnknown3;

	unsigned char				m_ucFormatType;
};

#endif