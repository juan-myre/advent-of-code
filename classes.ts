export interface EntityDto {
  id?: number
}

export class EntityBody implements EntityDto {
  public id?: number;
}

export interface CompanyDto extends EntityDto {
  name?: string
}

export class CompanyBody extends EntityBody implements CompanyDto {
  public name?: string;
}

export interface CompanyCreateDto extends Omit<CompanyDto, 'id'> {
}

export class CompanyCreateBody extends CompanyBody implements CompanyCreateDto{
}

export class Shau implements EntityDto {

}
