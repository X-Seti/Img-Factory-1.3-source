#ifndef CMvecIMGManager_H
#define CMvecIMGManager_H

#include "CIMGFile.h"
#include <vector>
#include <unordered_map>

struct HMENU__;
typedef HMENU__* HMENU;

class CGTAToolsGUIDlg;
class CViewInstance;
class CWnd;

struct CSearchEntry
{
	CViewInstance*				m_pViewInstance;
	CIMGEntry*					m_pIMGEntry;
};

class CMvecIMGManager
{
public:
	CMvecIMGManager(void) :
		m_pActiveViewInstance(nullptr)
	{
		for (unsigned long i = 0; i < 11; i++)
		{
			m_uiSortOptions[i] = 0xFFFFFFFF;
		}
	};

	void						setDialog(CGTAToolsGUIDlg *pDialog) { m_pDialog = pDialog; }
	CGTAToolsGUIDlg*			getDialog(void) { return m_pDialog; }

	void						init(void);

	void						onRequestOpen(void);
	void						onRequestOpen2(std::string strPath);
	void						onRequestClose(void);
	void						onRequestCloseAll(void);
	void						onRequestExitTool(void);
	void						onRequestImportViaFiles(void);
	void						onRequestRemoveSelected(void);
	void						onRequestRename(void);
	void						onRequestSelectAll(void);
	void						onRequestSelectInverse(void);
	void						onRequestRebuild(void);
	void						onRequestRebuildAs(void);
	void						onRequestRebuildAll(void);
	void						onRequestConvert(eIMGVersion eIMGVersion);
	void						onRequestConvertViaButton(void);
	void						onRequestMerge(void);
	void						onRequestSplit(void);
	void						onRequestReplace(void);
	void						onRequestExportSelected(void);
	void						onRequestSearchText(void);
	void						onRequestSearchSelection(void);
	void						onRequestFilter(void);
	void						onRequestFind(bool bFindInAllOpenedFiles = false);
	void						onRequestExportViaButton(void);
	void						onRequestExportViaIDEFile(void);
	void						onRequestExportViaTextLines(void);
	void						onRequestSortEntries(void);
	void						onRequestSortButton(void);
	void						onRequestRemoveViaIDEFile(void);
	void						onRequestRemoveViaTextLines(void);
	void						onRequestRemoveViaButton(void);
	void						onRequestImportViaButton(void);
	void						onRequestImportViaIDEFile(void);
	void						onRequestImportViaTextLines(void);

	void						onDropFile(std::string strPath);

	void						addViewInstance(std::string strIMGPath, eIMGVersion eIMGVersion);
	void						removeViewInstance(CViewInstance *pViewInstance);
	unsigned long				getViewInstanceCount(void) { return m_vecViewInstances.size(); }
	CViewInstance*				getViewInstanceByIndex(unsigned long uiIndex) { return m_vecViewInstances[uiIndex]; }
	std::vector<CViewInstance*>&	getViewInstances(void) { return m_vecViewInstances; }

	void						setActiveViewInstance(CViewInstance *pViewInstance);
	CViewInstance*				getActiveViewInstance(void) { return m_pActiveViewInstance; }

	void						addRecentlyOpenedFile(std::string strIMGPath);
	bool						doesRecentlyOpenedFileExist(std::string strIMGPath);
	void						loadRecentlyOpenedFiles(void);

	int							getMainListControlItemByEntry(CIMGEntry *pIMGEntry);

	HMENU						m_hSubMenu_File_OpenRecent;
	HMENU						m_hMenu_EntryOperations_Sort;
	std::vector<std::string>	m_vecSortByIDEEntries[10];
	std::vector<std::string>	m_vecSortByCOLEntries[10];
	std::vector<std::string>	m_vecSortByFileExtensions[10];
	std::unordered_map<unsigned long, std::string>	m_umapRecentlyOpenedFiles;

	unsigned long				m_uiSortOptions[11];
	unsigned long				m_uiSortOptionsIndex;

	std::vector<CSearchEntry*>	m_vecSearchEntries;

private:
	void						initDialog(void);

	CGTAToolsGUIDlg*			m_pDialog;
	std::vector<CViewInstance*>	m_vecViewInstances;
	CViewInstance*				m_pActiveViewInstance;
};

#endif