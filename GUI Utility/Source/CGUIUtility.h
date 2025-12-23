#ifndef CGUIUtility_H
#define CGUIUtility_H

#include <string>
#include <vector>

struct CTextInputDialogData
{
	std::string			m_strWindowTitle;
	std::string			m_strStaticText;
	std::string			m_strResultText;
};

struct CConvertDialogData
{
	bool				m_bRadioButtonSelected;
	unsigned long		m_uiRadioButtonIndex;
};

struct CExportViaDialogData
{
	bool				m_bRadioButtonSelected;
	unsigned long		m_uiRadioButtonIndex;
};

struct CSortOptionsDialogData
{
	std::vector<int>	m_vecSortOptions;
};

class CGUIUtility
{
public:
	static std::vector<std::string>			openFileDialog(std::string strDefaultPath = "");
	static std::string						saveFileDialog(std::string strDefaultPath = "");
	static std::string						saveFolderDialog(HWND hParentHwnd, std::string strTitle, std::string strDefaultPath = "");
	static std::string						showTextAreaDialog(HWND hParentHwnd, std::string strWindowTitle, std::string strStaticText);
	static std::string						showTextInputDialog(HWND hParentHwnd, std::string strWindowTitle, std::string strStaticText);
	static unsigned long					showConvertDialog(HWND hParentHwnd);
	static unsigned long					showExportViaDialog(HWND hParentHwnd);
	static std::vector<int>					showSortOptionsDialog(HWND hParentHwnd);
	static unsigned long					showRemoveViaDialog(HWND hParentHwnd);
	static unsigned long					showImportViaDialog(HWND hParentHwnd);
};

#endif